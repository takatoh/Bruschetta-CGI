#!/usr/bin/env ruby
# encoding: utf-8

require 'cgi'
require 'erb'


@cgi = CGI.new


def main
  index
end


def index
  @title = "Bruschetta CGI"
  @message = "Hello, from ERB!"
  template = File.read("./views/index.erb")
  erb = ERB.new(template)

  print_header
  print erb.result
end


def print_header
  print "content-type: text/html\n\n"
end



main
