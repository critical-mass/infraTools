**OKTA CHEATSHEET**

This is a collection of helpful Okta api endpoints, expressions and other info for doing administrative and development work
<br><br/>


**Okta expression language**

Leverage nickName name over firstName while available (displayName)

```
user.nickName != "" AND user.nickName != null ? user.nickName + " " + user.lastName : user.firstName + " " + user.lastName
```

Leverage nickName over firstName when available

```
user.nickName != "" AND user.nickName != null ? user.nickName : user.firstName
```

Set a group rule to look for blank profile details

```
user.oktaAttributeHere==null
```

Set a group rule to require two attributes to be met for pass

```
String.stringContains(user.attribute, "{attribute_here}") AND user.attribute=="{attribute_here}"
```

Set multiple variables for a group rule

```
Arrays.contains({"attribute0", "attribute1", "attribute2"}, user.attribute)
```

<br/><br/>

**API Endpoints**

GET Signon Policies (Global Session Policy):

```
/api/v1/policies?type=OKTA_SIGN_ON
```

GET MFA Enrollment Policies:

```
/api/v1/policies?type=MFA_ENROLL
```

GET Password Policies:

```
/api/v1/policies?type=PASSWORD
```

GET Access Policies (Authentication Policies):

```
/api/v1/policies?type=ACCESS_POLICY
```

GET Policy Rule:

```
/api/v1/policies/{{policyId}}/rules/{{ruleId}}
```

Get Authenticators (Available Factors)

```
/api/v1/authenticators
```

POST Activate user (send email)

```
/api/v1/users/{{userId}}/lifecycle/activate?sendEmail=true
```

POST Re-Activate user (send email)

```
/api/v1/users/{{userId}}/lifecycle/reactivate?sendEmail=true
```

<br/><br/>

**Okta Workflows**

Webhooks: Need to save the flow before being able to access the endpoint
<br/><br/>

**BambooHR (BHR)**

Prestart interval: how far in the future the importer will look
<br><br/>
Preferred Name: nickname
<br><br/>
