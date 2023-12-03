from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User
import requests

class GitHubTokenAuthentication(BaseAuthentication):
    api_allowed_github_teams = ['admin', 'mentors']
    github_organization_name = 'fuchicorp'

    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Token '):
            return None

        token = auth_header.split('Token ')[1]
        github_user = self.get_github_user_info(token)

        if not github_user:
            raise AuthenticationFailed('Invalid GitHub token.')

        try:
            user = User.objects.get(username=github_user['login'])
            if self.is_owner_in_admin_team(token, github_user):
                return user, None
            else:
                raise AuthenticationFailed('The user not part of api allowed teams')

        except User.DoesNotExist:
            raise AuthenticationFailed('The user does not exist in academy')


    def get_github_user_info(self, token):
        headers = {
            'Authorization': f'token {token}',
        }
        response = requests.get('https://api.github.com/user', headers=headers)
        if response.status_code == 200:
            return response.json()
        return None

    def get_organization_teams(self, token):
        headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        url = f'https://api.github.com/orgs/{self.github_organization_name}/teams'
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_team_members(self, token, team_slug):
        headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        url = f'https://api.github.com/orgs/{self.github_organization_name}/teams/{team_slug}/members'
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def is_owner_in_admin_team(self, token, github_user):
        for team_slug in self.api_allowed_github_teams:
            github_team_members = self.get_team_members(token, team_slug)
            for allowed_user in github_team_members:
                if allowed_user['login'] == github_user['login']:
                    return True
        return False
