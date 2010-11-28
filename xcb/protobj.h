#ifndef XPYB_PROTOBJ_H
#define XPYB_PROTOBJ_H

#include "conn.h"

typedef struct {
    PyObject_HEAD
    PyObject *buf;
    void *data;
} xpybProtobj;

extern PyTypeObject xpybProtobj_type;

extern PyTypeObject *xpybError_type;
extern PyTypeObject *xpybEvent_type;
extern PyTypeObject *xpybReply_type;
extern PyTypeObject *xpybRequest_type;
extern PyTypeObject *xpybStruct_type;

int xpybRequest_get_attributes(PyObject *request, int *is_void, int *opcode, int *is_checked);
int xpybError_set(xpybConn *conn, xcb_generic_error_t *e);
PyObject *xpybEvent_create(xpybConn *conn, xcb_generic_event_t *e);

int xpybProtobj_modinit(PyObject *m);

#endif
