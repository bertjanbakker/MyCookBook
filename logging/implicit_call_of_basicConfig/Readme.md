This example shows that using the root logger before calling basicConfig is a mistake
because basicConfig will then be called implicitly with default values.

Once basicConfig is called, subsequent calls to it will have no effect.
