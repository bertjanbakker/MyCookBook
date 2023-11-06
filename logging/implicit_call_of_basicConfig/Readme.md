This example shows that using the root logger before calling basicConfig is a mistake
because basicConfig will then be called implicitly with default values.

Once basicConfig is called, subsequent calls to it will have no effect.

Note that this could also happen by importing modules that cause basicConfig to be called.
