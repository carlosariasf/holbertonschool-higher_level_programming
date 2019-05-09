#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - print pytho inf
 * @p: PyObject
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t sizel, i;
	Py_ssize_t mema;
	PyObject *my_pyo;
	const char *typeo;

	sizel = PyList_Size(p);
	mema = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %li\n", sizel);
	printf("[*] Allocated = %li\n", mema);

	for (i = 0; i < sizel; i++)
	{
		my_pyo = PyList_GetItem(p, i);
		typeo = Py_TYPE(my_pyo)->tp_name;
		printf("Element %li: %s\n", i, typeo);
	}
}
