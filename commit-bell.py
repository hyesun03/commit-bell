from slacker import Slacker
import github3
import datetime
import pytz
import os

local_tz = pytz.timezone('Asia/Seoul')
token = os.environ.get('SLACK_BOT_COMMIT_BELL_TOKEN')
slack = Slacker(token)
channels = ['#study_unity', '#bot_test']

def post_to_channel(message):
    slack.chat.post_message(channels[1], message, as_user=True)

def get_repo_last_commit_delta_time(owner, repo):
    repo = github3.repository(owner, repo)
    return repo.pushed_at.astimezone(local_tz)

def get_delta_time(last_commit):
    now = datetime.datetime.now(local_tz)
    delta = now - last_commit
    return delta.days

def main():
    members = (
        ('songjongmoon', 'unity-study', '송종문'),
        ('eunsooJeon', 'unity', '전은수'),
        ('net9keep', 'unity', '함태영'),
        ('Oeno', 'tcpBird', '이송열'),
        ('janpro0706', 'tcp-unity-study', '장현동'),
        ('mommy79', 'TCP_Unity', '서바울'),
        ('KUvH', 'tcp_study_unity', '김현욱')
    )
    reports = []

    for owner, repo, name in members:
        last_commit = get_repo_last_commit_delta_time(owner, repo)
        delta_time = get_delta_time(last_commit)

        if(delta_time == 0):
            reports.append('*%s* 님은 오늘 커밋을 하셨어요!' % (name))
        else:
            reports.append('*%s* 님은 *%s* 일이나 커밋을 안하셨어요!' % (name, delta_time))

    post_to_channel('\n 안녕 친구들! <!here> 과제 점검하는 커밋벨이에요 호호 \n' + '\n'.join(reports))

if __name__ == '__main__':
    main()

