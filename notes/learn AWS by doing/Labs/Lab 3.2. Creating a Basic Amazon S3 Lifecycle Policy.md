# Creating a Basic Amazon S3 Lifecycle Policy

## Introduction

AWS Glacier is a long-term archive storage service that provides lower-cost storage than other AWS storage options. When data has not been accessed for a certain period of time, it can be moved automatically between S3 storage classes using a lifecycle policy. In this lab, we will create a basic Amazon S3 lifecycle policy.

## Solution

Log in to the AWS Management Console using the credentials provided on the lab instructions page. Make sure you're using the `us-east-1` region.

Feel free to [download the *pinehead.jpg* file](https://github.com/tia-la/ccp) if you'd like to upload it to the folder we'll create.

### Create an S3 Bucket and Upload an Object

1. Navigate to S3.
2. Click **Create bucket**.
3. For *Bucket name*, type "lalifecycle". (Since bucket names must be globally unique, add a series of random numbers at the end.)
4. Un-check *Block all public access*.
5. Check to acknowledge that the current settings might result in the bucket and the objects within it becoming public.
6. Click **Create bucket**.
7. Click the name of the bucket to open it, and then click **+ Create folder**.
8. Name the folder "MyProject", and click **Save**.
9. Open the folder, and click **Upload**.
10. Upload any file you'd like (which could be the *pinehead.jpg* file if you downloaded that from GitHub).
11. Click **Next**.
12. Under *Manage public permissions*, select **Grant public read access to this object(s)**.
13. Click **Next** > **Next** > **Upload**.

### Create a Lifecycle Policy

1. Click the bucket name at the top of the page.

2. Select the **Management** tab.

3. Click **+ Add lifecycle rule**.

4. Name the rule "s3toGlacier".

5. Under *Choose a rule scope*, select **Apply to all objects in the bucket**.

6. Click **Next**.

7. On the *Storage class transition* screen, check the boxes next to **Current version** and **Previous versions**.

8. Next to For current versions of objects, click **+Add transition**, and set the following values:

   - *Object creation*: **Transition to Glacier after**
   - *Days after creation*: **30** days

9. Check to acknowledge that this lifecycle rule will increase the one-time lifecycle request cost if it transitions small objects.

10. Next to For previous versions of objects, click +Add transition, and set the following values:

    - *Object becomes a previous version*: **Transition to Glacier Deep Archive after**
    - *Days after objects become noncurrent*: **15** days

11. Check to acknowledge that this lifecycle rule will increase the one-time lifecycle request cost if it transitions small objects.

12. Click **Next**.

13. On the *Configure expiration* screen, check **Previous versions**.

14. With **Permanently delete previous versions** checked, type "365" in to indicate they should delete after 365 days from becoming a previous version.

15. Click **Next**.

16. Check the box to acknowledge the lifecycle rule will apply to all objects in the bucket.

17. Click **Save**.

## Conclusion

Congratulations on completing this hands-on lab!