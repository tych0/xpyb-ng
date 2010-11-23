#include "module.h"
#include "except.h"
#include "event.h"

/*
 * Helpers
 */

PyObject *
xpybEvent_create(xpybConn *conn, xcb_generic_event_t *e)
{
    unsigned char opcode = e->response_type;
    PyObject *shim, *event, *type = (PyObject *)xpybEvent_type;

    if (opcode < conn->events_len && conn->events[opcode] != NULL)
	type = conn->events[opcode];

    shim = PyBuffer_FromMemory(e, sizeof(*e));
    if (shim == NULL)
	return NULL;

    event = PyObject_CallFunctionObjArgs(type, shim, NULL);
    Py_DECREF(shim);
    return event;
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

PyTypeObject *xpybEvent_type;

/*
 * Module init
 */
int xpybEvent_modinit(PyObject *m)
{
    PyObject *module = PyImport_ImportModule("xcb.response");
    if (!module)
        return -1;

    xpybEvent_type = (PyTypeObject *) PyObject_GetAttrString(module, "Event");
    Py_INCREF(xpybEvent_type);

    return 0;
}
