const mongoose = require('mongoose');

const DebateSchema = new mongoose.Schema({
  question: { type: String, required: true },
  researcher: { type: String, default: '' },
  analyst: { type: String, default: '' },
  critic: { type: String, default: '' },
  synthesizer: { type: String, default: '' },
  finalAnswer: { type: String, default: '' },
  status: { type: String, enum: ['pending', 'complete', 'failed'], default: 'pending' },
  createdAt: { type: Date, default: Date.now },
}, {
  versionKey: false,
});

module.exports = mongoose.model('Debate', DebateSchema);
