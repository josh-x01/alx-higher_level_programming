#include <stdio.h>
#include <Python.h>

void print_python_list_info(PyObject *p)
{
	int len = 0, idx;
	PyObject *item;

	len = Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

	for (idx = 0; idx < len; idx++)
	{
		item = PyList_GetItem(p, idx);
		printf("Element %d: %s\n", idx, Py_TYPE(item)->tp_name);
	}
}
