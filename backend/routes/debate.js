const express = require('express');
const router = express.Router();
const debateController = require('../controllers/debateController');

router.post('/', debateController.createDebate);
router.get('/', debateController.getDebates);
router.get('/:id', debateController.getDebateById);

module.exports = router;
