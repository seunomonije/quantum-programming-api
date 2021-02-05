CC = g++
FLAGS1 = -c -std=c++11 -fPIC
FLAGS2 = -shared -Wl,-install_name

all:
	$(CC) $(FLAGS1) IntArray.cpp -o IntArray.o
	$(CC) $(FLAGS2),libIntArray.so -o libIntArray.so  IntArray.o

	$(CC) $(FLAGS1) Playground.cpp -o Playground.o
	$(CC) $(FLAGS2),libPlayground.so -o libPlayground.so  Playground.o

clean:
	-rm *.o *.so all
	