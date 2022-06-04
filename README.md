
# The older version of the redstone library

> This project is _slightly_ outdated, not recommended to use for complex redstone projects.

## Examples

Powering on a lamp

```
import redstone

redstone.lever(True)
redstone.dust()
redstone.out("lamp")
```

Inverting the input

```
import redstone

redstone.lever(True)
redstone.dust()
redstone.torch()
redstone.out("lamp")
```

Delays

```
import redstone

redstone.lever(True)
redstone.repeater(1)
redstone.dust()
redstone.out("lamp")
```

thats pretty much it
