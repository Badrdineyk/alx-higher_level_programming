#include <Python.h>

/**
 * print_python_list_info - Prints some basic info about Python lists.
 * @p: PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int s; 
	int all;
	int i;
	PyObject *obj;

	s = Py_SIZE(p);
	all = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", s);
	printf("[*] Allocated = %d\n", all);

	for (i = 0; i < s; i++)
	{
		printf("Element %d: ", i);
		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
