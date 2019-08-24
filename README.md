# LINE-Notify-SNS-Consumer

This project is using AWS SQS to send LINE Notify message.

# Bebore you start

- LINE Notify token [LINE document](https://notify-bot.line.me/doc/en/)
- AWS secret key

# Enviroments

- Python 3.7
- Node 12.4.0
- Npm 6.9.0
- Serverless 1.45.1

# Quick Start

1. Install serverless via npm

```bash=
$ npm install -g serverless
```

2. Setup your **AWS** ceritficate

```bash=
export AWS_ACCESS_KEY_ID=<your-key-here>
export AWS_SECRET_ACCESS_KEY=<your-secret-key-here>
```

3. Clone this project

```bash=
$ serverless install --url https://github.com/louis70109/line-notify-sns-consumer -n <YOUR_FILE_NAME>
$ cd <YOUR_FILE_NAME>/
```

4. Replace LINE notify token and SQS Url in `sender.py`

```javascript=
output = {
  message: sys.argv[1],
  token: "Bearer YOUR_LINE_NOTIFY_TOKEN"
};
send_message(
  (url = "YOUR_AWS_SQS_URL"),
  (attr = {}),
  (body = json.dumps(output))
);
```

5. Deploy the webhhok function

```bash=
npm install
pip install -r requirements.txt
serverless deploy
```

# Author

Create by NiJia

# License

The project is available as open source under the terms of the MIT License.
