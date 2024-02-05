#include <Python.h>

/**
 * print_python_list - prints some basic info about Python lists
 * @p: PyObject list object.
 */
void print_python_list(PyObject *p)
{
	const char *t;
	Py_ssize_t s, mem_alloc, index;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	s = var->ob_size;
	mem_alloc = list->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", s);
	printf("[*] Allocated = %ld\n", mem_alloc);

	for (index = 0; index < s; index++)
	{
		t = list->ob_item[index]->ob_type->tp_name;
		printf("Element %ld: %s\n", index, t);
		if (strcmp(t, "bytes") == 0)
			print_python_bytes(list->ob_item[index]);
		else if (strcmp(t, "float") == 0)
			print_python_float(list->ob_item[index]);
	}
}

/**
 * print_python_bytes - prints some basic info about Python bytes
 * @p: PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t index;
	Py_ssize_t s;
	PyBytesObject *bytes = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  s: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size >= 10)
		s = 10;
	else
		s = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %ld bytes: ", s);
	for (index = 0; index < s; index++)
	{
		printf("%02hhx", bytes->ob_sval[index]);
		if (index == (s - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - print some basic info about Python float objects.
 * @p: PyObject float object.
 */
void print_python_float(PyObject *p)
{
	char *buff = NULL;

	PyFloatObject *float_obj = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	buff = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buff);
	PyMem_Free(buff);
}
