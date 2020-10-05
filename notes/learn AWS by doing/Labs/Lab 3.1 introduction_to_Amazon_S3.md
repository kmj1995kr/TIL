## Introduction to Amazon S3

In this Learning Activity, we are going to learn how to work with Amazon S3 buckets. Start by signing in to your lab environment using the provided username and password. Once you are logged in, search for 'S3' under AWS Services - this will take you to the Amazon S3 homepage.

### Creating an S3 Bucket

Click on the *Create bucket* button, enter your DNS-compliant bucket name into the 'Bucket name' space provided.

*Note: Bucket names must be globally unique. This means that if an AWS s3 user has a bucket named 'my-bucket-15556', nobody else can create and name a bucket called 'my-bucket-15556'.*

Select the *Region* in which you want your bucket to be stored. For instance, `us-east-1 (N. Virginia)`. Leave the 'copy settings from an existing bucket' section blank, since we do not have any existing bucket. Click *Next* to proceed to the *Set properties* page. Click *Versioning*, select *Enable Versioning*, then *Save*.

Click the *Next* button again to proceed to 'Set Permissions' page. We want to leave the bucket as private, so we do not change 'Manage public permissions'. We will also not modify the 'Manage System permissions'. Click on *Next* to proceed to the *Review* page. Review all the bucket settings and click on *Create bucket*.

#### Upload an Object to Amazon S3

Start by downloading the file `fountain.jpg` from the learning activity description to your computer.

Go back to the AWS S3 homepage and click on the name of your bucket 'my-bucket-15556' (or the name that you entered), Select *Upload* and click on *Add files*. Navigate to the directory where you saved the `fountain.jpg` file and select it. Click *Next* to proceed to *Set Permissions* page, leave all settings here as default and click on *Next* to proceed to the *Storage Class* page. We'll leave everything under *Storage class* as default and click on *Next* to review the settings. Click *Upload*.

Select the uploaded file `fountain.jpg` from the bucket dashboard and a window will pop up at the right-hand corner displaying all of the configured properties of the file.

Click on the S3 public link provided under *Overview* to view the content of the file. You should get an 'Access denied' message.

#### Creating Read Permission on an Object

Select the object `fountain.jpg`, right click on the object, scroll down and select *Make Public*. A small window will pop up. Confirm by clicking on *Make Public*.

Navigate back to the object page, click on the object `fountain.jpg` and click on the public link. You should see a beautiful picture of a fountain.

#### Showing the Different Versions

Again, click the object `fountain.jpg`, under the *Overview* tab, select *Show* (next to Version) to display the versions of the object. Right-click on `fountain.jpg` and select *Delete*. Navigate back to the *show version* to view the different versions that existed.

Right-click on the first version, select *Download* and save it to your computer.

We can now go back to the bucket and confirm that `fountain.jpg` has been deleted. Since we were able to download it via versioning, we can re-upload the file again. Click *Upload*, navigate to the directory where you saved the downloaded file, select the file, `fountain.jpg`, and click *Next* through to review and click *Upload file*.

Select `fountain.jpg` and click on the S3 public link to view the content. This time, you should get an 'Access denied' message.

## Re-Setting the Public Permission

Click on the object `fountain.jpg`, under the *Overview* tab, and select *Make Public* to set the public permission. Navigate back to the bucket home page, click your bucket and select *Show Version*. You should see the first version, the delete marker and the latest version.

### Applying a Bucket Policy

Next, we will learn how to set bucket policies to Amazon S3 buckets. In our example, we'll provide anonymous access to the bucket.

Click the link in the instructions of this activity to take you to a GitHub page. Open it up and copy the text.

Navigate back to Amazon S3 management console. Click on S3 and click the bucket name. A small pop up window will appear on the right corner. Select *Permissions* and click on *Bucket policy*. Paste in the prior text copied from the GitHub page. Modify the *Resources* part of the policy by coping and pasting the ARN for the bucket and hit *Save*.

You should get a warning notification prompting you that any object in your bucket will be public.

Let's go back into the bucket and upload another file. Select the bucket name, click on *Upload*, rename the old file to `fountain-new.jpg`, and upload it. Now click on `fountain-new.jpg` and then click on the public link. You should see the beautiful fountain picture again!

Congratulations! You've completed this Learning Activity! Once both boxes have been checked off on your dashboard, you can click "Grade Activity" and move on.