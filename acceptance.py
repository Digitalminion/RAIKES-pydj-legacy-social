#Tie together Social authentication with local authentication


##Facebook Confirm Oauth Token


##Create new User when the Social id does not exist

    def test_creation():
        #Assertions

        #preset Conditions
        #As a User                                      <-- Who would validate success
        user = austin leahy
        existingfacebookuser = {name: "austin", uuid: "12456sdg1"}

        ## passed to us from theoretical app
        social.Network = "facebook"
        social.Token = "asd#@%ADSagas123"

        #validate that a user doesn't exist
        #as an administrator curl account endpoint and see if the user exists
        #if it does exist conditions for test don't exist so kick back failure or setup conditions

        #expectation
        #I Want my account to be created automatically  <-- What will be acomplished
                                                                # (should be the sum of the unit tests or tasks)

         #     create the user using passin
        response = curl (login, {social})

        #asuming we got a token as a response validate the user was created

        response = curl (account, {social})

        #if that succeed then test passes


        #facebook response:
        validuser = {name: "austin", uuid: "12456sdg1"}
        #process response:
        localUser =  {name: "austin", uuid: "1"}



        #end result
        #So that I can start using the app right away   <-- How we measure success

        #final response:
        response = {authtoken:"2365asdgdga"}

        require:
            login endpoint
            account endpoint
