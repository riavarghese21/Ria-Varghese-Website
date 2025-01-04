const express = require('express');
const bodyParser = require('body-parser');
const nodemailer = require('nodemailer');
const path = require('path');

const app = express();

// Middleware to parse form data
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

// Serve static files from the project directory
app.use(express.static(path.join(__dirname)));

// Handle form submission
app.post('/send-message', (req, res) => {
    const { name, email, message } = req.body;

    // Set up Nodemailer transporter
    const transporter = nodemailer.createTransport({
        service: 'gmail', // Use your email provider
        auth: {
            user: 'riavarghese021@gmail.com', 
            pass: 'vosc qxrs phbv vrsj'  
        }
    });

    // Email details
    const mailOptions = {
        from: email,
        to: 'riavarghese021@gmail.com',
        subject: `Message from ${name}`,
        text: message
    };

    // Send email
    transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            console.error(error);
            return res.status(500).send('Error sending message.');
        }
        console.log('Email sent: ' + info.response);
        res.status(200).send('Message sent successfully!');
    });
});

// Start the server
app.listen(3000, () => {
    console.log('Server running at http://localhost:3000');
});

const links = document.querySelectorAll('.nav-links a');

links.forEach(link => {
  link.addEventListener('click', (e) => {
    e.preventDefault();
    const targetId = e.target.getAttribute('href').substring(1);
    document.getElementById(targetId).scrollIntoView({
      behavior: 'smooth',
      block: 'start',
    });
  });
});
