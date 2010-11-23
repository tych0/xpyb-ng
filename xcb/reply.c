#include "module.h"
#include "except.h"
#include "response.h"
#include "reply.h"

/*
 * Helpers
 */


/*
 * Infrastructure
 */


/*
 * Members
 */

/*
 * Definition
 */

PyTypeObject *xpybReply_type;

/*
 * Module init
 */
int xpybReply_modinit(PyObject *m)
{
    PyObject *module = PyImport_ImportModule("xcb.response");
    if (!module)
        return -1;

    xpybReply_type = (PyTypeObject *) PyObject_GetAttrString(module, "Reply");
    Py_INCREF(xpybReply_type);

    return 0;
}
