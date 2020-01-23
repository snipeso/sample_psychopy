from config.updateConfig import UpdateConfig

sampleCONF = {
    "task": {
        "name": "sample",
    },
    "instructions": {
        "text": "Give instructions",
        "startPrompt": "Press any key to continue. Press q to quit.",
    },
    "stimuli": {
        "backgroundColor": {"versionMain": "black", "versionDemo": "blue", "versionDebug": "gray"},
    },
    "sounds": {
        "alarm": "horn.wav",
    }
}

sampleTriggers = {
    "example": 10
}


updateCofig = UpdateConfig()
updateCofig.addContent(sampleCONF)
updateCofig.addTriggers(sampleTriggers)

CONF = updateCofig.getConfig()
