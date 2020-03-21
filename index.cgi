#!/usr/bin/env ruby
# encoding: utf-8

require 'cgi'
require 'erb'
require 'httpclient'
require 'json'


@cgi = CGI.new
@client = HTTPClient.new


def main
  index
end


def index
  @title = "Bruschetta CGI"
  json = @client.get("http://bruschetta/api/books/?limit=25").body
  @books = JSON.parse(json)["books"]
  template = File.read("./views/index.erb")
  erb = ERB.new(template)

  print_header
  print erb.result
end


def print_header
  print "content-type: text/html\n\n"
end



main
