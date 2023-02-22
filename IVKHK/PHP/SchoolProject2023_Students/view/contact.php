<?php
    ob_start();
    include_once('contactHeader.php');
?>


<div class="container">
    <div class="row">
        <div class="col-md-9 col-md-offset-1">
            <div class="well well-sm">
<form class="form horizontal" action="sendContact" method="post">
            <fieldset>
                <legend class="text-center">Contact us</legend>
                <div class="form-group">
                    <label class="col-md-3 control-label" for="name">Name</label>
                    <div class="col-md-9">
<input id="name" name="name" type="text" placeholder="Your name" class="form-control" required>
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-md-3 control-label" for="email">Your E-mail</label>
                    <div class="col-md-9">
<input id="email" name="email" type="text" placeholder="Your email" class="form-control" required>
                    </div>
                </div>
                <div class="form_group">
                    <label class="col-md-3 control-label" for="message">Your message</label>
                    <div class="col-md-9">
<textarea class="form-control" id="message" name="message" placeholder="Please enter your message here..." rows="5" required>
</textarea>
                    </div>
                </div>
                <div class="form-group">
                    <div class="col-md-12 text-right">
<button type="submit" class="btn-succes btn-lg" name="send">Send Message</button>
                    </div>
                </div>
            </fieldset>
            </form>
        </div>
    </div>
</div>
</div>
</article>
</div>
<?php
    $content=ob_get_clean();
    include 'view/templates/layout.php';
?>