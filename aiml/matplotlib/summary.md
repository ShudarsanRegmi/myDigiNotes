# Matplotlib

>Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. 


# Initialize
```
import matplot.pyplt as plt
import numpy as np
```

# Prepare
```
x = np.linspace(0, 10*np.pi, 1000) # create 1000 values between 0 and 10PI
y = np.sin(x)
```

# Setting Graph Parameters
```
plt.xlabel('xlabel')
plt.ylabel('ylabel')
```

# Render
plt.plot()
plt.grid()
plt.show()


# Subplot
>Subplots can be used to create multiple plots in a single figure


