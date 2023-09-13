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

int main() {
    Py_Initialize();
    PyObject *s = Py_BuildValue("y", "Hello");
    PyObject *b = Py_BuildValue("y", "\xff\xf8\x00\x00\x00\x00\x00\x00");
    PyObject *l = PyList_New(0);

    PyList_Append(l, s);
    PyList_Append(l, b);

    print_python_bytes(s);
    print_python_bytes(b);
    print_python_list(l);

    Py_DECREF(s);
    Py_DECREF(b);
    Py_DECREF(l);
    Py_Finalize();

    return 0;
}
