#include "module.h"
#include "except.h"
#include "response.h"
#include "error.h"

/*
 * Helpers
 */

int
xpybError_set(xpybConn *conn, xcb_generic_error_t *e)
{
    unsigned char opcode;
    PyObject *shim, *error, *type, *except;

    type = (PyObject *)xpybError_type;
    except = xpybExcept_proto;

    if (e) {
	opcode = e->error_code;
	if (opcode < conn->errors_len && conn->errors[opcode] != NULL) {
	    type = PyTuple_GET_ITEM(conn->errors[opcode], 0);
	    except = PyTuple_GET_ITEM(conn->errors[opcode], 1);
	}

	shim = PyBuffer_FromMemory(e, sizeof(*e));
	if (shim == NULL)
	    return 1;

	error = PyObject_CallFunctionObjArgs(type, shim, NULL);
	if (error != NULL)
	    PyErr_SetObject(except, error);
	Py_DECREF(shim);
	return 1;
    }
    return 0;
}


/*
 * Infrastructure
 */


/*
 * Members
 */


/*
 * Definition
 */

PyTypeObject *xpybError_type;

/*
 * Module init
 */
int xpybError_modinit(PyObject *m)
{
    PyObject *module = PyImport_ImportModule("xcb.response");
    if (!module)
        return -1;

    xpybError_type = (PyTypeObject *) PyObject_GetAttrString(module, "Error");
    Py_INCREF(xpybError_type);

    return 0;
}
