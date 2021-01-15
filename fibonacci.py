{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter any number5\n",
      "0 1 1 2 3 "
     ]
    }
   ],
   "source": [
    "#write a python program for fibonacci numbers\n",
    "num = int(input(\"Enter any number\"))\n",
    "a=0\n",
    "b=1\n",
    "i=0\n",
    "while i<num:\n",
    "    if num==0:\n",
    "        print(\"enter any number greayer than 0\")\n",
    "    elif num==1:\n",
    "        print(a)\n",
    "    else:\n",
    "        while i<num:\n",
    "             print(a,end=\" \")\n",
    "             new=a+b\n",
    "             a=b\n",
    "             b=new\n",
    "             i=i+1 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
