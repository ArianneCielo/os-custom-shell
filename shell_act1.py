import os
import sys


def main():
    while True:
        try:
            sys.stdout.write("py-sh> ")
            sys.stdout.flush()

            line = sys.stdin.readline()

            if line == "":
                break

            line = line.rstrip()
            args = line.split()

            if not args:
                continue

            command = " ".join(args)

            pid = os.fork()

            if pid == 0:
                child_pid = os.getpid()
                parent_pid = os.getppid()

                print(
                    f"[CHILD] PID: {child_pid} | "
                    f"PPID: {parent_pid} | "
                    f"Target: {command}",
                    flush=True
                )

                os._exit(0)

            elif pid > 0:
                parent_pid = os.getpid()

                print(
                    f"[PARENT] Spawned child with PID: {pid} | "
                    f"Shell PID: {parent_pid}",
                    flush=True
                )

            else:
                print(
                    "Error: os.fork() returned a negative value.",
                    file=sys.stderr
                )

        except EOFError:
            break

        except KeyboardInterrupt:
            print()
            break

        except OSError as error:
            print(f"Fork error: {error}", file=sys.stderr)

    print("Exiting py-sh.")


if __name__ == "__main__":
    main()
