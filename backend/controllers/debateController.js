const Debate = require('../models/Debate');

exports.createDebate = async (req, res) => {
  try {
    const { question, researcher, analyst, critic, synthesizer, finalAnswer } = req.body;
    const debate = await Debate.create({
      question,
      researcher,
      analyst,
      critic,
      synthesizer,
      finalAnswer,
      status: finalAnswer ? 'complete' : 'pending',
    });
    res.status(201).json(debate);
  } catch (error) {
    console.error('createDebate', error);
    res.status(500).json({ message: 'Internal server error' });
  }
};

exports.getDebates = async (req, res) => {
  try {
    const debates = await Debate.find().sort({ createdAt: -1 });
    res.status(200).json(debates);
  } catch (error) {
    console.error('getDebates', error);
    res.status(500).json({ message: 'Internal server error' });
  }
};

exports.getDebateById = async (req, res) => {
  try {
    const { id } = req.params;
    const debate = await Debate.findById(id);
    if (!debate) return res.status(404).json({ message: 'Debate not found' });
    res.status(200).json(debate);
  } catch (error) {
    console.error('getDebateById', error);
    res.status(500).json({ message: 'Internal server error' });
  }
};
