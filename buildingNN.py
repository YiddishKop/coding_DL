import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense

import numpy as np

np.arange()

## 模型构建
model = Sequential()
# input_dim 中存储的就是样本的维度，只在第一层hiddenlayer需要设置。
# units 中存储的就是这一层的神经元的个数. 
# input_dim 和 units 数目之间没有必然关系，因为两者之间还有参数矩阵做为连接。
model.add(Dense(input_dim = 28*28, units=500, activation = 'relu'))
# 第二层 hidden layer 以及之后的 layer 就完全没有必要声明 input_dim 了。
# 因为上一层的 hidden layer 的 units 的数目就是下一层的 hidden layer 的 input_dim
# 这在连接两个 hidden layer 时是默认去做的事情。
model.add(Dense(units = 500,  activation = 'relu'))
# 最后一层的 hidden layer 的 units 的维度必须与你想要的输出维度一致。
# 最后一层的激活函数一般选择 softmax 来提供某种概率的近似。
model.add(Dense(units=10, activation = 'softmax'))

## 配置
# 需要设置 loss， optimizer， metrics(衡量矩阵)
model.compile(loss='cagetorical crossentropy', 
              optimizer='adam', 
              metrics=['accuracy'])

## 训练
# 喂给模型的数据必须都是 numpy.array 的形式
model.fit(x_train, y_train, batch_size=100, epochs=20)

## 保存和加载模型
# 略

## 模型评价
# evaluate 函数会输出一个二维向量：
# 第一维表示在 testing data 上的 loss
# 第二维表示在 testing data 上的 正确率
score = model.evaluate(x_test, y_test)
print('Total loss', score[0])
print('accuracy', )

## 模型预测
result = model.predict(x_test)
