{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1c9821c4-d9f8-4628-b60b-e84e630d9ccd",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Programming Assignment #3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "21a4ef40-db67-48ca-88e8-c4d018839e6b",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Problem #2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2e5c43b2-e58a-4d54-948d-eb2744c82909",
   "metadata": {},
   "outputs": [],
   "source": [
    "#A."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "94a33ddc-2097-4dd5-a40c-89dd281dad9c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "2c834ea7-2f99-4523-8aa8-129643242c27",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "First 5 odd-numbered columns of all cars\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'cars' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[5], line 2\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mFirst 5 odd-numbered columns of all cars\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m----> 2\u001b[0m oddcars \u001b[38;5;241m=\u001b[39m cars\u001b[38;5;241m.\u001b[39miloc[\u001b[38;5;241m0\u001b[39m:\u001b[38;5;241m5\u001b[39m,[\u001b[38;5;241m1\u001b[39m,\u001b[38;5;241m3\u001b[39m,\u001b[38;5;241m5\u001b[39m,\u001b[38;5;241m7\u001b[39m,\u001b[38;5;241m9\u001b[39m,\u001b[38;5;241m11\u001b[39m]]\n\u001b[0;32m      3\u001b[0m oddcars\n",
      "\u001b[1;31mNameError\u001b[0m: name 'cars' is not defined"
     ]
    }
   ],
   "source": [
    "print(\"First 5 odd-numbered columns of all cars\")\n",
    "oddcars = cars.iloc[0:5,[1,3,5,7,9,11]]\n",
    "oddcars"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "789cca2a-5f2d-467c-9d64-5c83f6702f66",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
