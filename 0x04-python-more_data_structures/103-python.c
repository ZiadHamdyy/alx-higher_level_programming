#define PY_SIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *string;

    if (!PyBytes_Check(p)) {
        printf("[.] bytes object info\n");
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_GET_SIZE(p);
    string = PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", string);

    printf("  first %d bytes: ", (int)(size > 10 ? 10 : size));
    for (i = 0; i < (size > 10 ? 10 : size); i++) {
        printf("%02x ", string[i] & 0xff);
    }
    printf("\n");
}

void print_python_list(PyObject *p) {
    PyListObject *list = (PyListObject *)p;
    Py_ssize_t size, i;

    size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < size; i++) {
        PyObject *element = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
        if (PyBytes_Check(element)) {
            print_python_bytes(element);
        }
    }
}
