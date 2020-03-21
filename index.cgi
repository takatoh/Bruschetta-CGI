#!/usr/bin/env ruby
# encoding: utf-8

require 'cgi'


@cgi = CGI.new


def main
  index
end


def index
  print "content-type: text/html\n\n"
  print <<EOL
<html>
  <head>
    <title>Bruschetta CGI</title>
  </head>
  <body>
    <h1>Bruschetta CGI</h1>
    <p>Hello!</p>
  </body>
</html>
EOL
end


main
