{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled1.ipynb",
      "version": "0.3.2",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/sujana2k9/ML-Public/blob/master/Untitled1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "metadata": {
        "id": "t4cvuqVt778K",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "'''a=np.array([2,3,6,7,8], dtype=int)\n",
        "print(a)\n",
        "b=np.array((2,3,4,5), dtype=int)\n",
        "print(b)\n",
        "print(a[0])\n",
        "print(b[0])\n",
        "b[0]=8\n",
        "print(b)\n",
        "b=np.array((2,3,4,5), dtype=int)\n",
        "c=np.exp(b)\n",
        "print(c)\n",
        "print(b[1])'''\n",
        "d= np.array([[1,2,3,4,5,6,7], [4,5,6,7,8,9,2], [1,2,3,4,5,6,7], [4,5,6,7,8,9,2]], dtype=int)\n",
        "print(d)\n",
        "print(d[1,2])\n",
        "print(d[[[0],[1]],[1,3,4]])\n",
        "print (d[[[0], [1], [3]], [0, 2]])\n",
        "print(d[3][1]) #same as below\n",
        "print(d[3,1]) # same as above line\n",
        "print(d[1:3],)\n",
        "print(d[1:3,1:3])"
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}