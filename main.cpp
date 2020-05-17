#include <python2.7/Python.h>


int
main(void)
{
    Py_Initialize();
    //PyRun_SimpleString("print('hello world from Python embedded')");
    FILE *pyscript = fopen("/boot/system/data/Awesome/Awesome.py", "r");
    
    PyRun_SimpleFile(pyscript, "Awesome");
    Py_Finalize();
    return 0;
}
