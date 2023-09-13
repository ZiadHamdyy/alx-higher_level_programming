#define PY_SIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p) {
    PyBytesObject *bytes = (PyBytesObject *)p;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    printf("  size: %zd\n", size);

    char *str = PyBytes_AsString(p);
    if (str == NULL) {
        printf("  trying string: <nil>\n");
    } else {
        printf("  trying string: %s\n", str);
    }

    printf("  first 10 bytes: ");
    for (Py_ssize_t i = 0; i < 10 && i < size; i++) {
        printf("%02x ", (unsigned char)str[i]);
    }
    printf("\n");
}

void print_python_list(PyObject *p) {
    PyListObject *list = (PyListObject *)p;

    printf("[*] Python list info\n");
    Py_ssize_t size = PyList_Size(p);
    printf("[*] Size of the Python List = %zd\n", size);

    Py_ssize_t allocated = list->allocated;
    printf("[*] Allocated = %zd\n", allocated);

    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %zd: ", i);
        if (PyBytes_Check(item)) {
            print_python_bytes(item);
        } else if (PyLong_Check(item)) {
            printf("int\n");
        } else if (PyFloat_Check(item)) {
            printf("float\n");
        } else if (PyTuple_Check(item)) {
            printf("tuple\n");
        } else if (PyList_Check(item)) {
            printf("list\n");
        } else if (PyUnicode_Check(item)) {
            printf("str\n");
        } else {
            printf("<other>\n");
        }
    }
}
