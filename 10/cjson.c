#include <stdlib.h>
#include <stdio.h>

#include <Python.h>


PyObject* cjson_loads(PyObject* self, PyObject* args) {
    const char* json_str;
    if (!PyArg_ParseTuple(args, "s", &json_str)) {
        return NULL;
    }

    PyObject* dict = PyDict_New();

    int len = strlen(json_str);
    int i = 0;
    while (i < len) {
        int key_start = -1;
        int key_end = -1;
        for (int j = i; j < len; j++) {
            if (json_str[j] == '"') {
                if (key_start == -1) {
                    key_start = j + 1;
                } else {
                    key_end = j;
                    break;
                }
            }
        }
        if (key_start == -1 || key_end == -1) {
            Py_DECREF(dict);
            PyErr_SetString(PyExc_ValueError, "Invalid JSON string: Missing key");
            return NULL;
        }
        PyObject* key = PyUnicode_FromStringAndSize(json_str + key_start, key_end - key_start);

        int value_start = -1;
        int value_end = -1;
        for (int j = key_end; j < len; j++) {
            if (json_str[j] == ':') {
                value_start = j + 1;
                break;
            }
        }
        if (value_start == -1) {
            Py_DECREF(dict);
            Py_DECREF(key);
            PyErr_SetString(PyExc_ValueError, "Invalid JSON string: Missing value");
            return NULL;
        }
        for (int j = value_start; j < len; j++) {
            if (json_str[j] == ',' || json_str[j] == '}') {
                value_end = j;
                break;
            }
        }
        if (value_end == -1) {
            Py_DECREF(dict);
            Py_DECREF(key);
            PyErr_SetString(PyExc_ValueError, "Invalid JSON string: Unterminated value");
            return NULL;
        }

        const char* value_str = json_str + value_start;
        int value_len = value_end - value_start;
        while (isspace((unsigned char)value_str[0]) && value_len > 0) {
            value_str++;
            value_len--;
        }
        while (isspace((unsigned char)value_str[value_len - 1]) && value_len > 0) {
            value_len--;
        }
        PyObject* value = PyUnicode_FromStringAndSize(value_str, value_len);

        PyObject* stripped_key = PyObject_Str(key);
        PyObject* stripped_value = PyObject_Str(value);

        const char* stripped_value_str = PyUnicode_AsUTF8(stripped_value);
        int stripped_value_len = strlen(stripped_value_str);
        if (stripped_value_len >= 2 && stripped_value_str[0] == '"' && stripped_value_str[stripped_value_len - 1] == '"') {
            stripped_value = PyUnicode_FromStringAndSize(stripped_value_str + 1, stripped_value_len - 2);
        }
        PyObject* numeric_value = PyLong_FromString(PyUnicode_AsUTF8(stripped_value), NULL, 0);
        if (numeric_value != NULL) {
            Py_DECREF(stripped_value);
            stripped_value = numeric_value;
        } else {
            PyErr_Clear();
        }

        PyDict_SetItem(dict, stripped_key, stripped_value);

        Py_DECREF(key);
        Py_DECREF(value);
        Py_DECREF(stripped_key);
        Py_DECREF(stripped_value);

        i = value_end + 1;
    }

    return dict;
}


PyObject* cjson_dumps(PyObject* self, PyObject* args) {
    PyObject* obj;
    if (!PyArg_ParseTuple(args, "O", &obj)) {
        return NULL;
    }

    if (!PyDict_Check(obj)) {
        PyErr_SetString(PyExc_TypeError, "Argument must be a dictionary");
        return NULL;
    }

    PyObject* json_str = PyUnicode_FromString("{");

    PyObject* items = PyDict_Items(obj);
    Py_ssize_t size = PyList_Size(items);
    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject* item = PyList_GetItem(items, i);

        PyObject* key = PyTuple_GetItem(item, 0);
        PyObject* value = PyTuple_GetItem(item, 1);

        PyObject* key_str = PyObject_Str(key);
        PyObject* value_str;

        if (PyLong_Check(value) || PyFloat_Check(value)) {
            value_str = PyObject_Str(value);
        } else {
            value_str = PyUnicode_FromFormat("\"%s\"", PyUnicode_AsUTF8(value));
        }

        PyObject* entry_str = PyUnicode_FromFormat("\"%s\": %s",
                                                   PyUnicode_AsUTF8(key_str),
                                                   PyUnicode_AsUTF8(value_str));

        Py_DECREF(key_str);
        Py_DECREF(value_str);

        PyUnicode_Append(&json_str, entry_str);
        Py_DECREF(entry_str);

        if (i < size - 1) {
            PyUnicode_Append(&json_str, PyUnicode_FromString(", "));
        }
    }

    Py_DECREF(items);

    PyUnicode_Append(&json_str, PyUnicode_FromString("}"));

    return json_str;
}


static PyMethodDef methods[] = {
    {"loads", cjson_loads, METH_VARARGS, "Loads json-like string and return dict."},
    {"dumps", cjson_dumps, METH_VARARGS, "Dumps dictionary as JSON string."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef cjsonsmodule = {
    PyModuleDef_HEAD_INIT,
    "cjson",
    "Module cjson.",
    -1,
    methods
};

PyMODINIT_FUNC PyInit_cjson(void)
{
    return PyModule_Create( &cjsonsmodule );
}

