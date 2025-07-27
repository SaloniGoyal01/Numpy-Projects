import numpy as np                    
import matplotlib.pyplot as plt      

# 🎨 Creating a 2D NumPy array to represent a happy face using 0s and 1s
# 0 = background pixel (light color), 1 = face pixel (darker color in colormap)
happy_face = np.array([
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],   # Top curve of the head
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],   # Full face row
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 1],   # Eyes (0 = eye holes)
    [1, 1, 0, 0, 1, 1, 0, 0, 1, 1],   # Eyes continue
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],   # Face
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # Mouth line begins (0s for mouth opening)
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],   # Curve of smile
    [1, 0, 0, 1, 1, 1, 1, 0, 0, 1],   # More smile curve
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],   # Mouth bottom
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0]    # Bottom curve of the face
])


plt.imshow(happy_face, cmap='YlOrBr')   # 'YlOrBr' = Yellow to Orange to Brown colors
plt.title("😊 Happy Face Emoji")       
plt.axis('off')                        
plt.show()                           
