<h1 align="center">Birthday Auto Email Sender </h1>

<p>
  A simple Python script that automatically sends personalized birthday emails.<br>
  <br>
  The script checks today's date against <code>birthdays.csv</code>, picks a random letter template,
  customizes it with the recipient's name, and sends it via mail SMTP.
</p>

<hr>

<h2> Features</h2>
<ul>
  <li> Reads recipient data from <code>birthdays.csv</code> (Name, Email, Month, Day).</li>
  <li> Automatically checks if today matches any birthday.</li>
  <li> Randomly selects one of 3 letter templates.</li>
  <li> Replaces <code>[NAME]</code> placeholder with actual name.</li>
  <li> Sends a personalized birthday email through Gmail SMTP.</li>
</ul>

<hr>


<h2> Project Structure</h2>
 
<pre>
📦 birthday-email-sender/
 ┣ 📂 letter_templates/    # Birthday message templates
 ┃ ┣ letter_1.txt
 ┃ ┣ letter_2.txt
 ┃ ┗ letter_3.txt
 ┣ 📜 birthdays.csv        # Recipient info (Name, Email, Month, Day)
 ┣ 📜 main.py              # Main script
 ┣ 📜 README.md            # Project documentation
</pre>

<hr>

<h2> Getting Started</h2>

<h3>1. Clone the repository</h3>

<h3>2. Install dependencies</h3>
<pre><code>pip install pandas
</code></pre>

<h3>3. Configure your mail</h3>
<p>In <code>main.py</code>, replace:</p>
<pre><code>my_email = "your@mail.com"
password = "your-app-password"
also you can configure smtp for other mails other then gmail
</code></pre>
<p><b>Important:</b> Use a mail <b>App Password</b>, not your real password.</p>

<h3>4. Prepare your data</h3>
<pre><code>Name,Email,month,day
Test,test@example.com,9,2
</code></pre>

<h3>5. Run the script</h3>
<pre><code>python main.py
</code></pre>

<hr>

<h2> Example Output</h2>
<p><b>Letter Template (<code>letter_1.txt</code>):</b></p>
<pre>
Dear [NAME],

Wishing you a wonderful birthday filled with happiness and joy! 🎂🥳
</pre>

<p><b>Email sent:</b></p>
<pre>
Subject: Happy Birthday

Dear NAME,

Wishing you a wonderful birthday filled with happiness and joy! 🎂🥳
</pre>

<hr>

<h2> Built With</h2>
<ul>
  <li>Python 3.9+</li>
  <li>pandas</li>
  <li>smtplib (built-in)</li>
</ul>

<hr>
<hr>

<h2> Contributing</h2>
<p>Contributions are welcome! To contribute:</p>
<ol>
  <li>Fork the repository</li>
  <li>Create a new branch</li>
  <li>Commit your changes</li>
  <li>Push to your branch</li>
  <li>Open a Pull Request</li>
</ol>
<hr>
