
# coding: utf-8

# In[5]:

import argparse

from apiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials

import httplib2
from oauth2client import client
from oauth2client import file
from oauth2client import tools



def get_service(api_name, api_version, scope, key_file_location,
                service_account_email):
  """Get a service that communicates to a Google API.

  Args:
    api_name: The name of the api to connect to.
    api_version: The api version to connect to.
    scope: A list auth scopes to authorize for the application.
    key_file_location: The path to a valid service account p12 key file.
    service_account_email: The service account email address.

  Returns:
    A service that is connected to the specified API.
  """

  f = open(key_file_location, 'rb')
  key = f.read()
  f.close()

  credentials = SignedJwtAssertionCredentials(service_account_email, key,
    scope=scope)

  http = credentials.authorize(httplib2.Http())

  # Build the service object.
  service = build(api_name, api_version, http=http)

  return service


def get_first_profile_id(service):
  # Use the Analytics service object to get the first profile id.

  # Get a list of all Google Analytics accounts for this user
  accounts = service.management().accounts().list().execute()

  if accounts.get('items'):
    # Get the first Google Analytics account.
    account = accounts.get('items')[0].get('id')

    # Get a list of all the properties for the first account.
    properties = service.management().webproperties().list(
        accountId=account).execute()

    if properties.get('items'):
      # Get the first property id.
      property = properties.get('items')[0].get('id')

      # Get a list of all views (profiles) for the first property.
      profiles = service.management().profiles().list(
          accountId=account,
          webPropertyId=property).execute()

      if profiles.get('items'):
        # return the first view (profile) id.
        return profiles.get('items')[0].get('id')

  return None


def get_results(service, profile_id, startd, endd, m):
  # Where startd, endd are start and end dates which follow YYYY-MM-DD
  # and m is the metric to return
  # Use the Analytics Service Object to query the Core Reporting API
  # for the number of sessions within the past seven days.
  #return service.data().ga().get(
   #   ids='ga:' + profile_id,
   #   start_date='7daysAgo',
   #   end_date='today',
   #   metrics='ga:sessions').execute()
   return service.data().ga().get(
      ids='ga:' + profile_id,
      start_date=startd,
      end_date=endd,
      metrics=m).execute()
	  
def get_results_wdim(service, profile_id, startd, endd, m, d):
  # Where startd, endd are start and end dates which follow YYYY-MM-DD
  # and m is the metric to return and d is the dimension
  # Use the Analytics Service Object to query the Core Reporting API
  # for the number of sessions within the past seven days.
  #return service.data().ga().get(
   #   ids='ga:' + profile_id,
   #   start_date='7daysAgo',
   #   end_date='today',
   #   metrics='ga:sessions').execute()
   return service.data().ga().get(
      ids='ga:' + profile_id,
      start_date=startd,
      end_date=endd,
      metrics=m, dimensions=d).execute()


def print_results(results):
  # Print data nicely for the user.
  if results:
    print 'View (Profile): %s' % results.get('profileInfo').get('profileName')
    print 'Total Sessions: %s' % results.get('rows')[0][0]

  else:
    print 'No results found'


def main():
  # Define the auth scopes to request.
  scope = ['https://www.googleapis.com/auth/analytics.readonly']

  # Use the developer console and replace the values with your
  # service account email and relative location of your key file.
  service_account_email = '764727577979-8f2hs2kgononjmp5hon4kbachecil7ju@developer.gserviceaccount.com'
  key_file_location = 'GA_client_secrets.p12'

  # Authenticate and construct service.
  service = get_service('analytics', 'v3', scope, key_file_location,
    service_account_email)
  #profile = get_first_profile_id(service)
  profile = "11464615" 
  print_results(get_results(service, profile))


if __name__ == '__main__':
  main()

