import sys, time

def typewriter(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)

def main():
    typewriter("\nHello, Singapore!\n")

main()