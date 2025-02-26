CC = g++
CFLAGS = -Wall
LDFLAGS = -lncurses
TARGET = snake

all: $(TARGET)

$(TARGET): snake.cpp
	$(CC) $(CFLAGS) -o $(TARGET) snake.cpp $(LDFLAGS)

clean:
	rm -f $(TARGET)
