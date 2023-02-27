# Operations

The way in which *genus* handles operations is similar to the way in which *PyTorch* handles layers and modules. In *genus*, all functionality is realized through classes that inherit from the `Operation` interface, implementing the `forward()` method. The `__call__` dunder in `Operation` is overwritten so that it calls the `forward()` method, as well as do some debug logging and other important functionality: this way, operations can be instantiated and then called directly on the inputs.

Operations are separated into three default classes: elementary operations, genetic operations, and meta operations. However, more operations can be created by the user by simply creating classes that inherit from `Operation` or some other pre-fabricated operation, and implement the necessary behaviour inside `forward()`.
