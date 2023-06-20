**Okta expression language**

Leverage preferred name over first name while available

```
appuser.preferredName != "" AND appuser.preferredName != null ? appuser.preferredName + " " + appuser.lastName : appuser.firstName + " " + appuser.lastName
```
Set a group rule to look for blank profile details

```
user.oktaAttributeHere==null
```



**Okta Workflows**


Webhooks: Need to save the flow before being able to access the endpoint
