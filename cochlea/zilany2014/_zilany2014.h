#ifndef __PYX_HAVE__cochlea__zilany2014___zilany2014
#define __PYX_HAVE__cochlea__zilany2014___zilany2014


#ifndef __PYX_HAVE_API__cochlea__zilany2014___zilany2014

#ifndef __PYX_EXTERN_C
  #ifdef __cplusplus
    #define __PYX_EXTERN_C extern "C"
  #else
    #define __PYX_EXTERN_C extern
  #endif
#endif

__PYX_EXTERN_C DL_IMPORT(double) *generate_random_numbers(long);
__PYX_EXTERN_C DL_IMPORT(double) *decimate(int, double *, int);
__PYX_EXTERN_C DL_IMPORT(double) *ffGn(int, double, double, double, double);

#endif /* !__PYX_HAVE_API__cochlea__zilany2014___zilany2014 */

#if PY_MAJOR_VERSION < 3
PyMODINIT_FUNC init_zilany2014(void);
#else
PyMODINIT_FUNC PyInit__zilany2014(void);
#endif

#endif /* !__PYX_HAVE__cochlea__zilany2014___zilany2014 */
