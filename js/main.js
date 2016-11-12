 firebase.initializeApp({
    apiKey: "AIzaSyCwkffwdd20bxKNFmlIRY6TCohl1-VqdBg",
    authDomain: "communitycash-6d2ed.firebaseapp.com",
    databaseURL: "https://communitycash-6d2ed.firebaseio.com",
    storageBucket: "communitycash-6d2ed.appspot.com",
    messagingSenderId: "736235734105"
  });
  var database = firebase.database();

  /*/
/* Helper Functions
/*/

String.prototype.hashCode = function(){
	var hash = 0;
	if (this.length == 0) return hash;
	for (i = 0; i < this.length; i++) {
		char = this.charCodeAt(i);
		hash = ((hash<<5)-hash)+char;
		hash = hash & hash;
	}
	return hash;
}
function hasClass(el, className) {
  if (el.classList)
	return el.classList.contains(className)
  else
	return !!el.className.match(new RegExp('(\\s|^)' + className + '(\\s|$)'))
}
function addClass(el, className) {
  if (el.classList)
	el.classList.add(className)
  else if (!hasClass(el, className)) el.className += " " + className
}
function removeClass(el, className) {
  if (el.classList)
	el.classList.remove(className)
  else if (hasClass(el, className)) {
	var reg = new RegExp('(\\s|^)' + className + '(\\s|$)')
	el.className=el.className.replace(reg, ' ')
  }
}
function isReal(el) {
	if (el != null && el != undefined && el != "") {
		return true;
	} else {
		return false;
	}
}
function validateEmail(email) {
  var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return re.test(email);
}

function firebaseLogin() {
	var email = document.querySelector('#email').value;
	database.ref('users/' + email.replace(/[@.]/g, "")).once('value').then(function(snapshot){
		userData = snapshot.val();
		if (userData === null) {
			document.querySelector('.error-message').innerHTML = 'That account does not exist.';
			removeClass(document.querySelector('.error-message'), 'hidden');
		} else {
			var password = document.querySelector('#password').value;
			console.log(password.hashCode());
			console.log(userData);
			if (email === userData.email && password.hashCode() == userData.password) {
				addClass(document.querySelector('.error-message'), 'hidden');
				firebase.auth().signInWithEmailAndPassword(userData.email, password).then(function(){
					landing.style.margin = "-100vh";
					setTimeout(function(){
						addClass(landing, 'hidden');
					}, 500);
					var snackbarData = {
						message: 'Login Successful',
						timeout: 2000
					};
					snackbarContainer.MaterialSnackbar.showSnackbar(snackbarData);
					document.querySelector('#email').value ='';
					document.querySelector('#password').value ='';
					document.querySelector('.error-message').innerHTML = '';
					addClass(document.querySelector('.error-message'), 'hidden');
					user = firebase.auth().currentUser;
					if (isReal(userData.username)) {
						userNameSpan.innerHTML = userData.username;
					} else if (isReal(user.email)) {
						userNameSpan.innerHTML = user.email;
					}
					if (isReal(userData.photoURL)) {
						profilePicture.src = userData.photoURL;
					} else {
						profilePicture.src = 'images/user.jpg'
					}
					window.localStorage.setItem("user", JSON.stringify(user));
					window.localStorage.setItem("userData", JSON.stringify(userData));
				}).catch(function(error) {
					if (error) {
						if (error.code === 'auth/user-not-found') {
							
						} else {
							console.error(error)
							document.querySelector('.error-message').innerHTML = error.message;
							removeClass(document.querySelector('.error-message'), 'hidden');
						}
					}
				});
			} else {
				document.querySelector('.error-message').innerHTML = 'That email and password combo is invalid.';
				removeClass(document.querySelector('.error-message'), 'hidden');
			}
		}
	}).catch(function(error){
		console.error(error);
	});
}

function firebaseLogout() {
	firebase.auth().signOut().then(function() {
		userNameSpan.innerHTML = "Log In";
		profilePicture.src = "images/user.jpg";
		addClass(adminAuth, 'hidden2');
		addClass(approveReportsNavButton, 'hidden2');
		addClass(approveTableCategorizationButton, 'hidden');
		addClass(resetReportButton, 'hidden');
		removeClass(navNecirLogin, 'hidden');
		addClass(settingsButton, 'hidden');
		addClass(navLogout, 'hidden');
		var snackbarData = {
			message: 'Logout Successful',
			timeout: 2000
		  };
		snackbarContainer.MaterialSnackbar.showSnackbar(snackbarData);
		window.localStorage.setItem("user", null);
		window.localStorage.setItem("userData", null);
	}, function(error) {
		var snackbarData = {
			message: 'Logout Unsuccessful',
			timeout: 2000
		  };
		snackbarContainer.MaterialSnackbar.showSnackbar(snackbarData);
		console.error(error);
	});
}

window.onload = function() {
	document.querySelector("#login-btn").addEventListener('click', function(){
		if (validateEmail(document.querySelector("#email").value)) {
			document.querySelector('.error-message').innerHTML = '';
			addClass(document.querySelector('.error-message'), 'hidden');
			firebaseLogin();
		} else {
			document.querySelector('.error-message').innerHTML = 'That email is not valid!';
			removeClass(document.querySelector('.error-message'), 'hidden');
		}
	});
}