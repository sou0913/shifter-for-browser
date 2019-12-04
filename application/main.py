from flask import Flask, render_template, request, redirect, send_from_directory
#関数を書いてるファイルを読み込んでみる
import shifter

app = Flask(__name__)

@app.route('/', methods=['GET'])
def top():
    return render_template('input.html',title='シフト作成')

@app.route('/info',methods=['POST'])
def info():
    year  = int(request.form['year'])
    month = int(request.form['month'])
    members = int(request.form['members'])
    holiday = int(request.form['holiday'])
    at_least = int(request.form['at_least'])
    at_holiday = int(request.form['at_holiday'])
    continuous = int(request.form['continuous'])
    result = shifter.makeShift2(year, month, members, holiday, at_least, at_holiday, continuous)
    if result == "fix":
        notice = "連勤数に修正が必要です"
        return render_template('input.html', notice=notice)
    elif result == "unable":
        notice = "見つかりませんでした…"
        return render_template("input.html", notice=notice)
    else:
        tag = result
        return redirect(f'/result/{tag}')

@app.route('/result/<int:tag>',methods=['GET'])
def result(tag):
    notice = "作成しました！"
    return render_template('result.html', notice=notice, id=tag)

@app.route('/download',methods=['POST'])
def download():
    id = int(request.form['id'])
    return send_from_directory('static/books/', f'book{id}.xlsx', as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)

