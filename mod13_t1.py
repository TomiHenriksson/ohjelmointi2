from flask import Flask, request


app = Flask(__name__)
@app.route("/summa")
def primenumber():
    args = request.args
    num = int(args.get("luku1"))
    isPrime = False
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                isPrime = True
                break
    if isPrime:
        isPrime = False
        # answer1 = print(num, "is not a prime number")
    else:
        isPrime = True
        # answer1 = print(num, "is a prime number")
    answer = {
        "Number" : num,
        "isPrime" : isPrime
    }
    return answer


app.run(use_reloader=True, host="127.0.0.1", port=3000)