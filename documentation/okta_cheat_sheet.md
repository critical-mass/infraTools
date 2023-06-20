**Okta expression language**

Leverage preferred name over first name while available
```
appuser.preferredName != "" AND appuser.preferredName != null ? appuser.preferredName + " " + appuser.lastName : appuser.firstName + " " + appuser.lastName
```
Set a group rule to look for blank profile details
```
user.oktaAttributeHere==null
```
<br/><br/> 

**API Endpoints**


GET Singon Policies (Global Session Policy)
```
/api/v1/policies?type=OKTA_SIGN_ON
```
GET MFA Enrollment Policies
```
/api/v1/policies?type=MFA_ENROLL
```
GET Password Policices 
```
/api/v1/policies?type=PASSWORD
```
Get Policy rule:
```
/api/v1/policies/{{policyId}}/rules/{{ruleId}}
```
<br/><br/> 

**Okta Workflows**
Webhooks: Need to save the flow before being able to access the endpoint
<br/><br/> 

**BambooHR (BHR)**

Prestart interval: how far in the future the importer will look
<br><br/>
Preferred Name: nickname
