#include <Python.h>

/**
 * print_python_bytes - Prints some basic info about Python byte objects.
 * @p: PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	unsigned char size;
	unsigned char index;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");

	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", size);

	for (index = 0; index < size; index++)
	{
		printf("%02hhx", bytes->ob_sval[index]);
		if (index == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_list - Prints some basic info about Python lists.
 * @p: PyObject list object.
 */
void print_python_list(PyObject *p)
{
	int all;
	int index;
	int size;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	all = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", all);

	for (index = 0; index < size; index++)
	{
		type = list->ob_item[index]->ob_type->tp_name;
		printf("Element %d: %s\n", index, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[index]);
	}
}
