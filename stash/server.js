const express = require('express');
const OpenAIApi = require('openai');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());
app.use(express.static('public')); // Serve static files from 'public' directory

const openai = new OpenAIApi({
  apiKey: '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',
});

app.post('/ask', async (req, res) => {
    try {
        const response = await openai.chat.completions.create({
            model: "gpt-3.5-turbo",
            messages: [{ role: 'user', content: req.body.query }],
        });
        res.json({ answer: response.data.choices[0].text.trim() });
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'An error occurred', details: error.message });
    }
});



const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
